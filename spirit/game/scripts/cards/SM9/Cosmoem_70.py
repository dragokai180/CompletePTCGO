from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='829b2f1e-fa53-5801-82d2-5e5285085de9',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmoem.Name',
    display_name='Cosmoem',
    searchable_by=['Cosmoem', 'Stage 1', 'Cosmoem'],
    subtypes=['Stage 1'],
    collector_number=70,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Cosmog.Name',
    family_id=789,
    abilities=[
        Attack(
            title='Nap',
            game_text='Heal 20 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            effect=standard_attack,
        ),
    ],
)
