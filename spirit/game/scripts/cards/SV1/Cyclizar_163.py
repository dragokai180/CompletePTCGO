from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='32766706-81d2-5193-b620-9a26fe9bae74',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizar.Name',
    display_name='Cyclizar',
    searchable_by=['Cyclizar', 'Basic', 'Cyclizar'],
    subtypes=['Basic'],
    collector_number=163,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=967,
    abilities=[
        Attack(
            title='Reckless Charge',
            game_text='This Pokémon also does 10 damage to itself.',
            cost={PokemonTypes.COLORLESS: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
