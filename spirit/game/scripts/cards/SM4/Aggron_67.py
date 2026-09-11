from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='477b02d8-07c0-523f-b8c9-029ae467e0b8',
    key='SM4',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Aggron.Name',
    display_name='Aggron',
    searchable_by=['Aggron', 'Stage 2', 'Aggron'],
    subtypes=['Stage 2'],
    collector_number=67,
    set_code='SM4',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name',
    family_id=304,
    abilities=[
        Attack(
            title='Revenge Cannon',
            game_text='This attack does 10 more damage for each damage counter on all of your Benched Pokémon.',
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Buster Swing',
            game_text="This attack's damage isn't affected by Resistance.",
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=standard_attack,
        ),
    ],
)
