from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='5c9456db-ca34-55a6-8277-6dadca057687',
    key='DM',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.Flygon.Name',
    display_name='Flygon',
    searchable_by=['Flygon', 'Stage 2', 'Flygon'],
    subtypes=['Stage 2'],
    collector_number=39,
    set_code='DM',
    regulation_mark=None,
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FAIRY,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.Vibrava.Name',
    family_id=328,
    abilities=[
        Ability(
            title='Dragon Guard',
            game_text="Prevent all effects of your opponent's attacks, except damage, done to your Dragon Pokémon. (Existing effects are not removed.)",
            passive=standard_passive("Prevent all effects of your opponent's attacks, except damage, done to your Dragon Pokémon. (Existing effects are not removed.)"),
        ),
        Attack(
            title='Sand Tomb',
            game_text="The Defending Pokémon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=110,
            effect=standard_attack,
        ),
    ],
)
