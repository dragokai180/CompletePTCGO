from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="72e6f102-1004-5c31-96ff-2e15cbd3cb33",
    key="MEP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MegaLucarioex.Name",
    display_name="Mega Lucario ex",
    searchable_by=["Mega Lucario ex", "Stage 1", "MegaLucarioex"],
    subtypes=["Stage 1"],
    collector_number=12,
    set_code="MEP",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=340,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    abilities=[
        Attack(
            title="Aura Jab",
            game_text="Attach up to 3 Basic [ [Fighting] ] Energy cards from your discard pile to your Benched Pokémon in any way you like.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=130,
            effect=standard_attack,
        ),
        Attack(
            title="Mega Brave",
            game_text="During your next turn, this Pokémon can't use Mega Brave.",
            cost={PokemonTypes.FIGHTING: 2},
            damage=270,
            effect=standard_attack,
            locks_next_turn=True,
        ),
    ],
)
