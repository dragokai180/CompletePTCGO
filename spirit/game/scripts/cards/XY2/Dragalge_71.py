from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='eb6e3716-4b6a-5969-8c87-5c8aa30e34ad',
    key='XY2',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Dragalge.Name',
    display_name='Dragalge',
    searchable_by=['Dragalge', 'Stage 1', 'Dragalge'],
    subtypes=['Stage 1'],
    collector_number=71,
    set_code='XY2',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=100,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Skrelp.Name',
    family_id=690,
    abilities=[
        Ability(
            title='Poison Barrier',
            game_text="Your opponent's Poisoned Pokémon can't retreat.",
            passive=standard_passive("Your opponent's Poisoned Pokémon can't retreat."),
        ),
        Attack(
            title='Poison Breath',
            game_text="Flip a coin. If heads, your opponent's Active Pokémon is now Poisoned.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
            effect=standard_attack,
        ),
    ],
)
