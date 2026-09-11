from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='d9263bc6-a13a-5975-b23f-841b56d11f7f',
    key='TATM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasLairon.Name',
    display_name="Team Magma's Lairon",
    searchable_by=["Team Magma's Lairon", 'Stage 1', 'TeamMagmasLairon'],
    subtypes=['Stage 1'],
    collector_number=13,
    set_code='TATM',
    regulation_mark=None,
    rarity=Rarities.Common,
    hp=90,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasAron.Name',
    family_id=304,
    abilities=[
        Attack(
            title='Gnaw',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
        Attack(
            title='Take Down',
            game_text='This Pokémon does 10 damage to itself.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
