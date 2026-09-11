from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='56a86969-a3e8-5dd7-8e58-79966a7aa190',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Lucario.Name',
    display_name='Lucario',
    searchable_by=['Lucario', 'Stage 1', 'Lucario'],
    subtypes=['Stage 1'],
    collector_number=117,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name',
    family_id=447,
    abilities=[
        Ability(
            title='Tag Coach',
            game_text="Your TAG TEAM Pokémon take 20 less damage from your opponent's attacks (after applying Weakness and Resistance).",
            passive=standard_passive("Your TAG TEAM Pokémon take 20 less damage from your opponent's attacks (after applying Weakness and Resistance)."),
        ),
        Attack(
            title='Mach Cross',
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)
