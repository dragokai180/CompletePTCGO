from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='b994cbad-1c05-5935-ac55-02130746ffee',
    key='SM11',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Carracosta.Name',
    display_name='Carracosta',
    searchable_by=['Carracosta', 'Stage 2', 'Carracosta'],
    subtypes=['Stage 2'],
    collector_number=45,
    set_code='SM11',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=160,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Tirtouga.Name',
    family_id=564,
    abilities=[
        Ability(
            title='Ancient Custom',
            game_text="Pokémon Tool cards attached to your opponent's Pokémon have no effect.",
            passive=standard_passive("Pokémon Tool cards attached to your opponent's Pokémon have no effect."),
        ),
        Attack(
            title='Aqua Impact',
            game_text="This attack does 20 more damage for each Colorless in your opponent's Active Pokémon's Retreat Cost.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
            damage_operator='+',
            effect=standard_attack,
        ),
    ],
)
