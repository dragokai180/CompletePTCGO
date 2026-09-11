from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='8e453d05-651d-5856-83f4-1be70d8afd4c',
    key='SV2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Vespiquen.Name',
    display_name='Vespiquen',
    searchable_by=['Vespiquen', 'Stage 1', 'Vespiquen'],
    subtypes=['Stage 1'],
    collector_number=9,
    set_code='SV2',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Combee.Name',
    family_id=415,
    abilities=[
        Attack(
            title='Double Stab',
            game_text='Flip 2 coins. This attack does 30 damage for each heads.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            damage_operator='x',
            effect=standard_attack,
        ),
        Attack(
            title='Order a Raid',
            game_text="Choose 1 of your Benched Combee and shuffle that Pokémon and all attached cards into your deck. If you can't shuffle a Combee into your deck, this attack does nothing.",
            cost={PokemonTypes.GRASS: 1},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
