from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='ef58dc18-0ff5-54dd-818f-15a8c07e62c8',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Spiritomb.Name',
    display_name='Spiritomb',
    searchable_by=['Spiritomb', 'Basic', 'Spiritomb'],
    subtypes=['Basic'],
    collector_number=158,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    family_id=442,
    abilities=[
        Ability(
            title='Fettered in Misfortune',
            game_text="Basic Pokémon V in play (both yours and your opponent's) have no Abilities.",
            passive=standard_passive("Basic Pokémon V in play (both yours and your opponent's) have no Abilities."),
        ),
        Attack(
            title='Fade Out',
            game_text='Put this Pokémon and all attached cards into your hand.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=10,
            effect=standard_attack,
        ),
    ],
)
