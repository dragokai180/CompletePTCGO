from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='980c2aa6-f9b8-5aab-bea5-2ce742cf0947',
    key='SM12',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lileep.Name',
    display_name='Lileep',
    searchable_by=['Lileep', 'Stage 1', 'Lileep'],
    subtypes=['Stage 1'],
    collector_number=10,
    set_code='SM12',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.UnidentifiedFossil.Name',
    family_id=345,
    abilities=[
        Attack(
            title='Confuse Ray',
            game_text="Your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.GRASS: 1},
            effect=standard_attack,
        ),
        Attack(
            title='Seed Bomb',
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
        ),
    ],
)
