from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='75c9fbed-8b12-5324-b1a6-024868df20fe',
    key='GUM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Arcanine.Name',
    display_name='Arcanine',
    searchable_by=['Arcanine', 'Stage 1', 'Arcanine'],
    subtypes=['Stage 1'],
    collector_number=6,
    set_code='GUM',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.WATER,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Growlithe.Name',
    family_id=59,
    abilities=[
        Ability(
            title='Security Guard',
            game_text="As long as this Pokémon is your Active Pokémon, all of your Pokémon take 30 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            passive=standard_passive("As long as this Pokémon is your Active Pokémon, all of your Pokémon take 30 less damage from your opponent's attacks (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Sharp Fang',
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
