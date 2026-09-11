from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7e1c3a15-943c-591b-b2a7-074ca85ea8c7',
    key='XY4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Hydreigon.Name',
    display_name='Hydreigon',
    searchable_by=['Hydreigon', 'Stage 2', 'Hydreigon'],
    subtypes=['Stage 2'],
    collector_number=74,
    set_code='XY4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zweilous.Name',
    family_id=633,
    abilities=[
        Ability(
            title='Dark Impulse',
            game_text='Once during your turn (before your attack), you may attach a Darkness Energy card from your discard pile to your Active Pokémon.',
            effect=standard_ability,
            activation=Activations.ONCE_PER_TURN,
        ),
        Attack(
            title='Crazy Headbutt',
            game_text='Discard an Energy attached to this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 2},
            damage=130,
            effect=standard_attack,
        ),
    ],
)
