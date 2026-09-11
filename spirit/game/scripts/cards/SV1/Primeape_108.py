from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='65680c10-9ac9-5b45-99cf-c50be2714dd2',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Primeape.Name',
    display_name='Primeape',
    searchable_by=['Primeape', 'Stage 1', 'Primeape'],
    subtypes=['Stage 1'],
    collector_number=108,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Mankey.Name',
    family_id=56,
    abilities=[
        Attack(
            title='Raging Punch',
            game_text='This Pokémon also does 20 damage to itself.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
