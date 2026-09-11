from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='4e2d4b51-c057-5e6d-8c0c-705062d9a3e6',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Linoone.Name',
    display_name='Linoone',
    searchable_by=['Linoone', 'Stage 1', 'Linoone'],
    subtypes=['Stage 1'],
    collector_number=168,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Zigzagoon.Name',
    family_id=263,
    abilities=[
        Attack(
            title='Jet Headbutt',
            cost={PokemonTypes.COLORLESS: 1},
            damage=40,
        ),
        Attack(
            title='Reckless Charge',
            game_text='This Pokémon also does 30 damage to itself.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=standard_attack,
        ),
    ],
)
