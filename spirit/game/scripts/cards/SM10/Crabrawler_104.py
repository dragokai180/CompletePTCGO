from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ef13290a-c858-522b-9f23-405e5aa0804e',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Crabrawler.Name',
    display_name='Crabrawler',
    searchable_by=['Crabrawler', 'Basic', 'Crabrawler'],
    subtypes=['Basic'],
    collector_number=104,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=80,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=739,
    abilities=[
        Attack(
            title='Corkscrew Punch',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Knuckle Blast',
            game_text='If you have more Prize cards remaining than your opponent, this attack does 60 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
