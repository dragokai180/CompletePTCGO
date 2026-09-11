from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5e59641e-6fdd-5ee1-92de-24a1384aeb93',
    key='SM10',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Gliscor.Name',
    display_name='Gliscor',
    searchable_by=['Gliscor', 'Stage 1', 'Gliscor'],
    subtypes=['Stage 1'],
    collector_number=99,
    set_code='SM10',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gligar.Name',
    family_id=207,
    abilities=[
        Attack(
            title='Collect',
            game_text='Draw 3 cards.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Poison Jab',
            game_text="Your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=70,
            effect=standard_attack,
        ),
    ],
)
