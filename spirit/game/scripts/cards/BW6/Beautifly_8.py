from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import (
    AttrID, CLIENT_POKEMON_TYPE_NAMES, PokemonStage, PokemonTypes, Rarities,
)
from spirit.game.card_effects.trainers import is_basic_energy_card
from spirit.game.card_effects.bw_era import bw_legacy_attack, bw_legacy_ability, bw_legacy_passive, bw_trainer_effect, bw_trainer_passive, bw_tool_abilities, bw_stadium_ability, bw_stadium_triggers

async def triple_energy(ctx):
    """Search your deck for 3 different types of basic Energy cards and attach
    them to your Pokémon in any way you like. Shuffle your deck afterward."""
    deck_cards = list(ctx.deck(ctx.player_id))
    reps = []
    labels = {}
    seen_types = []
    for card in deck_cards:
        if not is_basic_energy_card(card):
            continue
        types = card.get_attribute(AttrID.POKEMON_TYPES) or []
        if not types or types[0] in seen_types:
            continue
        seen_types.append(types[0])
        reps.append(card)
        labels[card.entity_id] = f"{CLIENT_POKEMON_TYPE_NAMES[PokemonTypes(types[0])]} Energy"

    # No matches still shows the deck browser (nothing selectable).
    picks = await ctx.choose_cards(
        reps, 3, minimum=0,
        prompt="Choose up to 3 basic Energy cards of different types.",
        display_cards=deck_cards,
    )
    for energy in picks:
        label = labels[energy.entity_id]
        target = await ctx.choose_pokemon(
            ctx.my_pokemon_in_play(), f"Choose a Pokémon to attach {label} to"
        )
        if target is not None:
            await ctx.attach_energy(energy, target)
    await ctx.shuffle_deck()



card = PokemonCardDef(
    guid="971ab21f-f516-55bc-b8ac-7b088af8b5bf",
    key="BW6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Beautifly.Name",
    display_name="Beautifly",
    searchable_by=["Beautifly","Stage 2","Beautifly"],
    subtypes=["Stage 2"],
    collector_number=8,
    set_code="BW6",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Silcoon.Name",
    abilities=[
        Attack(
            title="Triple Energy",
            game_text="Search your deck for 3 different types of basic Energy cards and attach them to your Pokémon in any way you like. Shuffle your deck afterward.",
            cost={PokemonTypes.GRASS: 1},
            effect=triple_energy,
        ),
        Attack(
            title="Drainpour",
            game_text="Heal 40 damage from each of your Benched Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            effect=bw_legacy_attack,
        ),
    ],
)
