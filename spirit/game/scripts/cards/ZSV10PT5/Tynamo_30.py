from spirit.game.data_utils import PokemonCardDef, Attack
from spirit.game.attributes import PokemonStage, PokemonTypes, Rarities
from spirit.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="2e81ae05-0e7d-5e6d-8472-5bc958b0f9b5",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    display_name="Tynamo",
    searchable_by=["Tynamo","Basic","Tynamo"],
    subtypes=["Basic"],
    collector_number=30,
    set_code="ZSV10PT5",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=602,
    abilities=[
        Attack(
            title="Hold Still",
            game_text="Heal 10 damage from this Pokémon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_attack(10),
        ),
    ],
)
