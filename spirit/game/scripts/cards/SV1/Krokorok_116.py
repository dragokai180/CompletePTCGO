from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2e3233a5-dc21-5fd7-a253-f935017536a0',
    key='SV1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Krokorok.Name',
    display_name='Krokorok',
    searchable_by=['Krokorok', 'Stage 1', 'Krokorok'],
    subtypes=['Stage 1'],
    collector_number=116,
    set_code='SV1',
    regulation_mark='G',
    rarity=Rarities.Common,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Sandile.Name',
    family_id=551,
    abilities=[
        Attack(
            title='Payback',
            game_text='If your opponent has exactly 1 Prize card remaining, this attack does 90 more damage.',
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Corkscrew Punch',
            cost={PokemonTypes.FIGHTING: 2},
            damage=60,
        ),
    ],
)
