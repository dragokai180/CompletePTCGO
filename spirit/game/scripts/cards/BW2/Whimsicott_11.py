from spirit.game.data_utils import PokemonCardDef, Attack, Ability
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.attacks_common import count_energy, damage_per
from spirit.game.card_effects.bw10 import barrier_attack, telekinesis_of_nobility
from spirit.game.card_effects.trainers import is_basic_energy_card

async def helping_hand(ctx):
    """Search your deck for a basic Energy card and attach it to 1 of your
    Benched Pokémon. Shuffle your deck afterward."""
    picks = await ctx.search_deck(
        is_basic_energy_card, count=1, minimum=0,
        prompt="Choose a basic Energy card to attach.",
    )
    await ctx.shuffle_deck()
    if not picks:
        return
    bench = ctx.my_bench()
    if not bench:
        return
    target = await ctx.choose_pokemon(bench, "Choose a Benched Pokémon to attach the Energy to")
    if target is not None:
        await ctx.attach_energy(picks[0], target)



card = PokemonCardDef(
    guid="b8d044a1-1a9c-5e56-bd18-98f4f336453a",
    key="BW2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Whimsicott.Name",
    display_name="Whimsicott",
    searchable_by=["Whimsicott","Stage 1","Whimsicott"],
    subtypes=["Stage 1"],
    collector_number=11,
    set_code="BW2",
    rarity=Rarities.Uncommon,
    hp=80,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Cottonee.Name",
    abilities=[
        Attack(
            title="Helping Hand",
            game_text="Search your deck for a basic Energy card and attach it to 1 of your Benched Pokémon. Shuffle your deck afterward.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=helping_hand,
        ),
        Attack(
            title="Cotton Guard",
            game_text="During your opponent's next turn, any damage done to this Pokémon by attacks is reduced by 30 (after applying Weakness and Resistance).",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            effect=barrier_attack,
        ),
    ],
)
