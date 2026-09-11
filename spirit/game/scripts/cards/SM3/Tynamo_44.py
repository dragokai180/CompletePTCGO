from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='c3ac3921-02c1-520e-8793-eaa2b934488a',
    key='SM3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name',
    display_name='Tynamo',
    searchable_by=['Tynamo', 'Basic', 'Tynamo'],
    subtypes=['Basic'],
    collector_number=44,
    set_code='SM3',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    resistance_type=PokemonTypes.METAL,
    resistance_amount=20,
    family_id=602,
    abilities=[
        Attack(
            title='Aqua Shock',
            game_text="If your opponent's Active Pokémon has any Water Energy attached to it, this attack does 30 more damage.",
            cost={PokemonTypes.LIGHTNING: 1},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
