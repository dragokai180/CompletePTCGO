from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b49d7f42-e18a-5092-b10c-4ad8a5fcd66b',
    key='XY10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Marowak.Name',
    display_name='Marowak',
    searchable_by=['Marowak', 'Stage 1', 'Marowak'],
    subtypes=['Stage 1'],
    collector_number=37,
    set_code='XY10',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cubone.Name',
    family_id=105,
    abilities=[
        Ability(
            title='Bodyguard',
            game_text="Prevent all effects of attacks done to you or your hand by your opponent's Pokémon. Remove any existing effects.",
            passive=standard_passive("Prevent all effects of attacks done to you or your hand by your opponent's Pokémon. Remove any existing effects."),
        ),
        Attack(
            title='Bonemerang',
            game_text='Flip 2 coins. This attack does 60 damage times the number of heads.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='x',
            effect=standard_attack,
        ),
    ],
)
