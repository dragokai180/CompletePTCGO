from spirit.game.data_utils import Attack, Ability, PokemonCardDef, Activations, Triggers
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities
from spirit.game.card_effects.standard_era import (
    standard_ability, standard_attack, standard_passive,
)


card = PokemonCardDef(
    guid='6b110e54-7146-5ca9-aca7-357a5b43bbf0',
    key='SM9',
    name='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanNinetales.Name',
    display_name='Alolan Ninetales',
    searchable_by=['Alolan Ninetales', 'Stage 1', 'AlolanNinetales'],
    subtypes=['Stage 1'],
    collector_number=111,
    set_code='SM9',
    regulation_mark=None,
    rarity=Rarities.RareHolo,
    hp=110,
    elements=[PokemonTypes.FAIRY],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.METAL,
    weakness_amount=2,
    evolves_from='com.direwolfdigital.cake.data.archetypes.pokemon.AlolanVulpix.Name',
    family_id=38,
    abilities=[
        Ability(
            title='Luminous Barrier',
            game_text="Prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Pokémon-GX or Pokémon-EX.",
            passive=standard_passive("Prevent all effects of attacks, including damage, done to this Pokémon by your opponent's Pokémon-GX or Pokémon-EX."),
        ),
        Attack(
            title='Aurora Beam',
            cost={PokemonTypes.FAIRY: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)
