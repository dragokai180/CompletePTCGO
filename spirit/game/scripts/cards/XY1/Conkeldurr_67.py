from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='430a6089-e42e-5b49-abdd-a43555c0d5ec',
    key='XY1',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Conkeldurr.Name',
    display_name='Conkeldurr',
    searchable_by=['Conkeldurr', 'Stage 2', 'Conkeldurr'],
    subtypes=['Stage 2'],
    collector_number=67,
    set_code='XY1',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gurdurr.Name',
    family_id=532,
    abilities=[
        Attack(
            title='Wake-Up Slap',
            game_text="If your opponent's Active Pokémon is affected by a Special Condition, this attack does 60 more damage. Then, remove all Special Conditions from that Pokémon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            damage_operator='+',
            effect=standard_attack,
        ),
        Attack(
            title='Dynamic Punch',
            game_text="Flip a coin. If heads, this attack does 40 more damage and your opponent's Active Pokémon is now Confused.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=60,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
