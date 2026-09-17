from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='a7d718cf-5adb-5a65-bfbf-08e51c34783a',
    key='ME55',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Pikachuex.Name',
    display_name='Pikachu ex',
    searchable_by=['Pikachu ex', 'Basic', 'ex', 'Pikachuex'],
    subtypes=['Basic', 'ex'],
    collector_number=54,
    set_code='ME55',
    regulation_mark='J',
    rarity=Rarities.RareHoloEX,
    hp=190,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    family_id=25,
    abilities=[
        Attack(
            title='Zip-Zap Frenzy',
            game_text='You may attach any number of Basic Energy cards from your hand to your Pokémon in any way you like.',
            cost={PokemonTypes.LIGHTNING: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Thunder',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.LIGHTNING: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=standard_attack,
        ),
    ],
)

from spirit.game.card_effects.thirtieth_celebration import configure
configure(card)
