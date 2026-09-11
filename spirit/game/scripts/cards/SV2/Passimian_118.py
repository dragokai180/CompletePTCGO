from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='79fbc177-b49c-5fa1-b002-78199331fe31',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Passimian.Name',
    display_name='Passimian',
    searchable_by=['Passimian', 'Basic', 'Passimian'],
    subtypes=['Basic'],
    collector_number=118,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    family_id=766,
    abilities=[
        Attack(
            title='Make the Assist',
            game_text='Move an Energy from this Pokémon to 1 of your Benched Pokémon.',
            cost={PokemonTypes.FIGHTING: 2},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
