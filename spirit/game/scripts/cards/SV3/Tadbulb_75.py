from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ddb58c36-2fde-5bca-ae07-adbbc0dc96eb',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Tadbulb.Name',
    display_name='Tadbulb',
    searchable_by=['Tadbulb', 'Basic', 'Tadbulb'],
    subtypes=['Basic'],
    collector_number=75,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=60,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=938,
    abilities=[
        Attack(
            title='Thunder Jolt',
            game_text='This Pokémon also does 10 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            effect=standard_attack,
        ),
    ],
)
