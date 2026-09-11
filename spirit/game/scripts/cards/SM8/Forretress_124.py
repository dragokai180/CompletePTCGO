from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='83118631-56da-5ddd-a574-f3457e464efa',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Forretress.Name',
    display_name='Forretress',
    searchable_by=['Forretress', 'Stage 1', 'Forretress'],
    subtypes=['Stage 1'],
    collector_number=124,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Pineco.Name',
    family_id=204,
    abilities=[
        Attack(
            title='Thorny Eruption',
            game_text="Flip 3 coins. This attack does 10 damage for each heads to each of your opponent's Pokémon. (Don't apply Weakness and Resistance for Benched Pokémon.)",
            cost={PokemonTypes.METAL: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Lost Blast',
            game_text='Put this Pokémon and all cards attached to it in the Lost Zone.',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=190,
            effect=standard_attack,
        ),
    ],
)
