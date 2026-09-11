from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='79261db0-abc5-50e0-a8ec-ce929a44ec2a',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name',
    display_name='Tynamo',
    searchable_by=['Tynamo', 'Basic', 'Tynamo'],
    subtypes=['Basic'],
    collector_number=64,
    set_code='SM11',
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
            title='Generate Electricity',
            game_text='Search your deck for a Lightning Energy card and attach it to this Pokémon. Then, shuffle your deck.',
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
    ],
)
