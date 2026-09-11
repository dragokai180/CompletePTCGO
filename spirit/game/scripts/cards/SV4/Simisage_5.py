from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='0abf85ea-2bea-5bd6-b8d4-6fa2c7915c90',
    key='SV4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Simisage.Name',
    display_name='Simisage',
    searchable_by=['Simisage', 'Stage 1', 'Simisage'],
    subtypes=['Stage 1'],
    collector_number=5,
    set_code='SV4',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pansage.Name',
    family_id=511,
    abilities=[
        Ability(
            title='Monkey Trio',
            game_text='If you have Simisage, Simisear, and Simipour in play, ignore all Colorless Energy in the costs of attacks used by this Pokémon.',
            passive=standard_passive('If you have Simisage, Simisear, and Simipour in play, ignore all Colorless Energy in the costs of attacks used by this Pokémon.'),
        ),
        Attack(
            title='Arm Thrust Needle',
            game_text="During your opponent's next turn, prevent all damage done to this Pokémon by attacks from Pokémon that have an Ability, except any Simisage.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=100,
            effect=standard_attack,
        ),
    ],
)
