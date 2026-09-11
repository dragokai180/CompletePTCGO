from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='e19ba5d0-52ba-5cee-8118-9660c7dd2974',
    key='SM5',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Solgaleo.Name',
    display_name='Solgaleo ◇',
    searchable_by=['Solgaleo ◇', 'Basic', 'Prism Star', 'Solgaleo'],
    subtypes=['Basic', 'Prism Star'],
    collector_number=89,
    set_code='SM5',
    regulation_mark=None,
    rarity=Rarities.Prism,
    hp=160,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    family_id=791,
    abilities=[
        Attack(
            title='Radiant Star',
            game_text="For each of your opponent's Pokémon in play, attach a Metal Energy card from your discard pile to your Pokémon in any way you like.",
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Corona Impact',
            game_text="This Pokémon can't attack during your next turn.",
            cost={PokemonTypes.METAL: 4},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
