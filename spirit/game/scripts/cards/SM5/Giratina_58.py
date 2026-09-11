from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='f6b0e098-bcc1-5e0e-b063-388ca18fff76',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Giratina.Name',
    display_name='Giratina ◇',
    searchable_by=['Giratina ◇', 'Basic', 'Prism Star', 'Giratina'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=58,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=160,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=20,
    family_id=487,
    abilities=[
        Ability(
            title='Chaotic Star',
            game_text='When you play this Pokémon from your hand onto your Bench during your turn, you may attach 2 Psychic Energy cards from your hand to it.',
            effect=standard_ability,
            trigger=Triggers.ON_PLAY,
        ),
        Attack(
            title='Crisis Dive',
            game_text='Discard 2 Energy from this Pokémon.',
            cost={PokemonTypes.PSYCHIC: 4},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
