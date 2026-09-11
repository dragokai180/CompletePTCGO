from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='462d0ada-3716-5a42-af94-e242f09ca9f6',
    key='SL',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Incineroar.Name',
    display_name='Incineroar',
    searchable_by=['Incineroar', 'Stage 2', 'Incineroar'],
    subtypes=['Stage 2'],
    collector_number=17,
    set_code='SL',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=170,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Torracat.Name',
    family_id=725,
    abilities=[
        Attack(
            title='Profane Punch',
            game_text='If your Benched Pokémon have any damage counters on them, this attack does 80 more damage.',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Flare Blitz',
            game_text='Discard all Fire Energy from this Pokémon.',
            cost={PokemonTypes.FIRE: 2, PokemonTypes.COLORLESS: 1},
            damage=180,
            effect=standard_attack,
        ),
    ],
)
