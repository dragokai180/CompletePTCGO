from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b292548d-d495-535f-9149-7ebecfb7dc0e',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Oinkologne.Name',
    display_name='Oinkologne',
    searchable_by=['Oinkologne', 'Stage 1', 'Oinkologne'],
    subtypes=['Stage 1'],
    collector_number=183,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lechonk.Name',
    family_id=915,
    abilities=[
        Attack(
            title='Confounding Cologne',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='High-Impact Kick',
            game_text='Flip a coin. If tails, this Pokémon also does 60 damage to itself.',
            cost={PokemonTypes.COLORLESS: 3},
            damage=160,
            effect=standard_attack,
        ),
    ],
)
