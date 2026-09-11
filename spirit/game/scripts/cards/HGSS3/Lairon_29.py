from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import AbilityTypes, PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='58cbff1a-8c78-5ddf-a651-1c4f2b3dc562',
    key='HGSS3',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lairon.Name',
    display_name='Lairon',
    searchable_by=['Lairon', 'Stage 1', 'Lairon'],
    subtypes=['Stage 1'],
    collector_number=29,
    set_code='HGSS3',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=90,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Aron.Name',
    family_id=304,
    abilities=[
        Attack(
            title='Scrap Attack',
            game_text='Flip a coin. If heads, search your discard pile for a Metal Energy card and attach it to Lairon.',
            cost={PokemonTypes.METAL: 1},
            damage=20,
            effect=standard_attack,
        ),
        Attack(
            title='Tackle',
            cost={PokemonTypes.METAL: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
