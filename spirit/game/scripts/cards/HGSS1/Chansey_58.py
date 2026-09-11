from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='095cfb6d-615d-5afa-8ceb-f10249f25914',
    key='HGSS1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Chansey.Name',
    display_name='Chansey',
    searchable_by=['Chansey', 'Basic', 'Chansey'],
    subtypes=['Basic'],
    collector_number=58,
    set_code='HGSS1',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=113,
    abilities=[
        Attack(
            title='Pound',
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
        ),
        Attack(
            title='Happy Punch',
            game_text='Flip a coin. If heads, remove 3 damage counters from Chansey.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            effect=standard_attack,
        ),
    ],
)
