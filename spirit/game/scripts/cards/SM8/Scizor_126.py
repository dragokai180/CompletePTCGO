from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='09cfa82f-17c4-5aaf-ab21-3d48f985769a',
    key='SM8',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Scizor.Name',
    display_name='Scizor',
    searchable_by=['Scizor', 'Stage 1', 'Scizor'],
    subtypes=['Stage 1'],
    collector_number=126,
    set_code='SM8',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    weakness_amount=2,
    resistance_type=PokemonTypes.PSYCHIC,
    resistance_amount=20,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Scyther.Name',
    family_id=123,
    abilities=[
        Ability(
            title='Exoskeleton',
            game_text='This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).',
            passive=standard_passive('This Pokémon takes 30 less damage from attacks (after applying Weakness and Resistance).'),
        ),
        Attack(
            title='Special Blow',
            game_text="If your opponent's Active Pokémon has any Special Energy attached to it, this attack does 70 more damage.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
