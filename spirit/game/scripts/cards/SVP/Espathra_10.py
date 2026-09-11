from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='7904a30e-e06b-5801-8e99-1beb08b2b15e',
    key='SVP',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Espathra.Name',
    display_name='Espathra',
    searchable_by=['Espathra', 'Stage 1', 'Espathra'],
    subtypes=['Stage 1'],
    collector_number=10,
    set_code='SVP',
    regulation_mark='G',
    rarity=Rarities.RarePromo,
    hp=110,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.DARKNESS,
    weakness_amount=2,
    resistance_type=PokemonTypes.FIGHTING,
    resistance_amount=30,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Flittle.Name',
    family_id=956,
    abilities=[
        Attack(
            title='Aurora Gain',
            game_text='Heal 30 damage from this Pokémon.',
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Super Psy Bolt',
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)
