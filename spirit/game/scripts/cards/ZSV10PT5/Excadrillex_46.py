from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="4b60f10a-d7c5-5fe5-aa06-a6ce10d8d111",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Excadrillex.Name",
    display_name="Excadrill ex",
    searchable_by=["Excadrill ex", "Stage 1", "ex", "Excadrillex"],
    subtypes=["Stage 1", "ex"],
    collector_number=46,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.RareHoloEX,
    hp=270,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drilbur.Name",
    family_id=529,
    abilities=[
        Attack(
            title="Piercing Drill",
            game_text="This attack also does 60 damage to 1 of your opponent's Benched Pokémon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
            effect=standard_attack,
        ),
        Attack(
            title="Rock Tumble",
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=200,
            effect=standard_attack,
        ),
    ],
)
