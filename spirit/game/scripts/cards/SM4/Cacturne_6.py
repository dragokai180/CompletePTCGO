from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='32a055c9-3ad8-5ccc-b456-dd1f1c268d6f',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cacturne.Name',
    display_name='Cacturne',
    searchable_by=['Cacturne', 'Stage 1', 'Cacturne'],
    subtypes=['Stage 1'],
    collector_number=6,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cacnea.Name',
    family_id=331,
    abilities=[
        Attack(
            title='Spike Rend',
            game_text="If your opponent's Active Pokémon already has any damage counters on it, this attack does 60 more damage.",
            cost={PokemonTypes.GRASS: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Hunt',
            game_text="Switch 1 of your opponent's Benched Pokémon with their Active Pokémon. This attack does 40 damage to the new Active Pokémon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
