from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="a24b185d-f729-50bc-96f7-52c5705c42f7",
    key="SV09",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesRibombee.Name",
    display_name="Lillie's Ribombee",
    searchable_by=["Lillie's Ribombee", "Stage 1", "LilliesRibombee"],
    subtypes=["Stage 1"],
    collector_number=67,
    set_code="SV09",
    regulation_mark="I",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.LilliesCutiefly.Name",
    family_id=742,
    abilities=[
        Ability(
            title="Inviting Wink",
            game_text="When you play this Pokémon from your hand to evolve 1 of your Pokémon during your turn, you may have your opponent reveal their hand and you put any number of Basic Pokémon you find there onto their Bench.",
            effect=standard_ability,
            trigger=Triggers.ON_EVOLVE,
        ),
        Attack(
            title="Magical Shot",
            cost={PokemonTypes.PSYCHIC: 1},
            damage=50,
        ),
    ],
)
