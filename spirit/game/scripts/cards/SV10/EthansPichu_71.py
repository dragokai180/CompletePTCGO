from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid="6b24a807-dec6-50fb-b088-67999e6fade3",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.EthansPichu.Name",
    display_name="Ethan's Pichu",
    searchable_by=["Ethan's Pichu", "Basic", "EthansPichu"],
    subtypes=["Basic"],
    collector_number=71,
    set_code="SV10",
    regulation_mark="I",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=172,
    abilities=[
        Attack(
            title="Zapping Draw",
            game_text="Draw a card.",
            cost={},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
