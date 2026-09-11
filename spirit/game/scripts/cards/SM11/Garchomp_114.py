from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='2f5c0bfa-8bf0-5cd3-8a9e-5cd4f2cd1667',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Garchomp.Name',
    display_name='Garchomp',
    searchable_by=['Garchomp', 'Stage 2', 'Garchomp'],
    subtypes=['Stage 2'],
    collector_number=114,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=150,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=0,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Gabite.Name',
    family_id=443,
    abilities=[
        Ability(
            title='Avenging Aura',
            game_text="If you have more Prize cards remaining than your opponent, this Pokémon's attacks do 80 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance).",
            passive=standard_passive("If you have more Prize cards remaining than your opponent, this Pokémon's attacks do 80 more damage to your opponent's Active Pokémon (before applying Weakness and Resistance)."),
        ),
        Attack(
            title='Over Slice',
            game_text='You may discard an Energy from this Pokémon. If you do, this attack does 40 more damage.',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
