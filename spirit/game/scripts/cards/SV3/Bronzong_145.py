from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='cc5a1d45-fee8-5c4c-a5d5-ec46a7cd9c96',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzong.Name',
    display_name='Bronzong',
    searchable_by=['Bronzong', 'Stage 1', 'Bronzong'],
    subtypes=['Stage 1'],
    collector_number=145,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.GRASS,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Bronzor.Name',
    family_id=436,
    abilities=[
        Attack(
            title='Oracle Press',
            game_text="During your opponent's next turn, prevent all effects of attacks used by your opponent's Pokémon done to this Pokémon. (Damage is not an effect.)",
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Extrasensory',
            game_text='If you have the same number of cards in your hand as your opponent, this attack does 90 more damage.',
            cost={PokemonTypes.METAL: 2},
            damage=70,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
