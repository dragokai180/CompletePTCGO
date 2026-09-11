from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6387e5a2-6488-5c44-996c-cf421dc06d31',
    key='SV045',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Grapploct.Name',
    display_name='Grapploct',
    searchable_by=['Grapploct', 'Stage 1', 'Grapploct'],
    subtypes=['Stage 1'],
    collector_number=52,
    set_code='SV045',
    regulation_mark='G',
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Clobbopus.Name',
    family_id=852,
    abilities=[
        Attack(
            title='Slow-Acting Syncope',
            game_text="At the end of your opponent's next turn, the Defending Pokémon will be Knocked Out.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=30,
            effect=standard_attack,
        ),
        Attack(
            title='Mach Cross',
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=120,
        ),
    ],
)
