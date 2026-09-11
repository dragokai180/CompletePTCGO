from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0057ac6a-92ab-5773-9dea-529ea3bb1535',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Simisear.Name',
    display_name='Simisear',
    searchable_by=['Simisear', 'Stage 1', 'Simisear'],
    subtypes=['Stage 1'],
    collector_number=21,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pansear.Name',
    family_id=513,
    abilities=[
        Ability(
            title='Monkey Trio',
            game_text='If you have Simisage, Simisear, and Simipour in play, ignore all Colorless Energy in the costs of attacks used by this Pokémon.',
            passive=standard_passive('If you have Simisage, Simisear, and Simipour in play, ignore all Colorless Energy in the costs of attacks used by this Pokémon.'),
        ),
        Attack(
            title='Heat Tackle',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 3},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
