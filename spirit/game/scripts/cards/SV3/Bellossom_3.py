from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='45a5a04f-4557-51a8-abfb-68070808f6c6',
    key='SV3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Bellossom.Name',
    display_name='Bellossom',
    searchable_by=['Bellossom', 'Stage 2', 'Bellossom'],
    subtypes=['Stage 2'],
    collector_number=3,
    set_code='SV3',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gloom.Name',
    family_id=43,
    abilities=[
        Attack(
            title='Sleep Powder',
            game_text="Your opponent's Active Pokémon is now Asleep.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Powerful Dance',
            game_text='Flip a coin for each Energy attached to this Pokémon. This attack does 90 damage for each heads.',
            cost={PokemonTypes.GRASS: 1},
            damage=90,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
